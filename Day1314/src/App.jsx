import { useCallback, useEffect, useState } from 'react'
import CineShelfApp from '@cineshelf/App.jsx'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

class ApiError extends Error {
  constructor(message, status) {
    super(message)
    this.status = status
  }
}

function currentRoute() {
  return window.location.hash === '#/dashboard' ? 'dashboard' : 'login'
}

function navigate(route) {
  window.location.hash = route === 'dashboard' ? '/dashboard' : '/login'
}

async function apiRequest(path, accessToken, options = {}) {
  const headers = new Headers(options.headers)
  if (options.body) headers.set('Content-Type', 'application/json')
  if (accessToken) headers.set('Authorization', `Bearer ${accessToken}`)

  let response
  try {
    response = await fetch(`${API_URL}${path}`, { ...options, headers })
  } catch (requestError) {
    if (requestError.name === 'AbortError') throw requestError
    throw new Error('Could not connect to CineShelf. Check that the backend is running.')
  }

  const result = response.status === 204
    ? null
    : await response.json().catch(() => null)

  if (!response.ok) {
    const detail = result?.detail
    const message = Array.isArray(detail)
      ? detail.map((issue) => issue.msg).join(' ')
      : typeof detail === 'string'
        ? detail
        : 'The request could not be completed.'
    throw new ApiError(message, response.status)
  }

  return result
}

function LoginForm({ onLogin }) {
  const [mode, setMode] = useState('login')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')

  async function handleSubmit(event) {
    event.preventDefault()
    setIsSubmitting(true)
    setError('')

    try {
      if (mode === 'register') {
        await apiRequest('/auth/register', '', {
          method: 'POST',
          body: JSON.stringify({ email, password }),
        })
      }

      const result = await apiRequest('/auth/login', '', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
      })
      onLogin(result.access_token)
    } catch (requestError) {
      setError(requestError instanceof Error
        ? requestError.message
        : 'Something went wrong. Please try again.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <section className="auth-card" aria-labelledby="auth-title">
      <p className="eyebrow">YOUR NEXT MOVIE NIGHT STARTS HERE</p>
      <h1 id="auth-title">{mode === 'login' ? 'Welcome back.' : 'Create your account.'}</h1>
      <p className="card-copy">
        {mode === 'login'
          ? 'Sign in to open your personal CineShelf.'
          : 'Register to make a secure CineShelf account.'}
      </p>

      <form className="auth-form" onSubmit={handleSubmit}>
        <label htmlFor="email">Email address</label>
        <input
          autoComplete="email"
          id="email"
          maxLength={254}
          onChange={(event) => setEmail(event.target.value)}
          placeholder="you@example.com"
          required
          type="email"
          value={email}
        />

        <label htmlFor="password">Password</label>
        <input
          autoComplete={mode === 'login' ? 'current-password' : 'new-password'}
          id="password"
          minLength={8}
          onChange={(event) => setPassword(event.target.value)}
          placeholder="At least 8 characters"
          required
          type="password"
          value={password}
        />

        {error && <p className="form-error" role="alert">{error}</p>}

        <button className="primary-button" disabled={isSubmitting} type="submit">
          {isSubmitting
            ? 'Please wait...'
            : mode === 'login' ? 'Sign in' : 'Create account'}
          {!isSubmitting && <span aria-hidden="true">→</span>}
        </button>
      </form>

      <p className="mode-switch">
        {mode === 'login' ? 'New to CineShelf?' : 'Already have an account?'}
        <button
          onClick={() => {
            setMode(mode === 'login' ? 'register' : 'login')
            setError('')
          }}
          type="button"
        >
          {mode === 'login' ? 'Create an account' : 'Sign in'}
        </button>
      </p>

      <p className="security-note">
        Passwords are hashed by the API. Your short-lived access token stays in
        memory and is sent only with CineShelf API requests.
      </p>
    </section>
  )
}

function AuthenticatedCineShelf({ accessToken, onLogout }) {
  const [user, setUser] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    const controller = new AbortController()

    async function verifySession() {
      try {
        const account = await apiRequest('/auth/me', accessToken, {
          signal: controller.signal,
        })
        setUser(account)
      } catch (requestError) {
        if (requestError.name === 'AbortError') return
        if (requestError.status === 401) {
          onLogout()
        } else {
          setError(requestError.message)
        }
      }
    }

    verifySession()
    return () => controller.abort()
  }, [accessToken, onLogout])

  if (error) {
    return (
      <main className="auth-page">
        <section className="auth-card" role="alert">
          <h1>Could not open CineShelf.</h1>
          <p className="card-copy">{error}</p>
          <button className="primary-button" onClick={onLogout} type="button">Return to sign in</button>
        </section>
      </main>
    )
  }

  if (!user) {
    return (
      <main className="auth-page">
        <p className="card-copy">Checking your sign-in...</p>
      </main>
    )
  }

  return (
    <CineShelfApp
      accessToken={accessToken}
      onLogout={onLogout}
      user={user}
    />
  )
}

export default function App() {
  const [route, setRoute] = useState(currentRoute)
  const [accessToken, setAccessToken] = useState('')

  useEffect(() => {
    function updateRoute() {
      setRoute(currentRoute())
    }

    window.addEventListener('hashchange', updateRoute)
    return () => window.removeEventListener('hashchange', updateRoute)
  }, [])

  function handleLogin(token) {
    setAccessToken(token)
    navigate('dashboard')
  }

  const handleLogout = useCallback(() => {
    setAccessToken('')
    navigate('login')
  }, [])

  if (route === 'dashboard' && accessToken) {
    return (
      <AuthenticatedCineShelf
        accessToken={accessToken}
        onLogout={handleLogout}
      />
    )
  }

  return (
    <main className="auth-page">
      <div className="ambient ambient-one" />
      <div className="ambient ambient-two" />
      <header className="auth-header">
        <a aria-label="CineShelf authentication demo home" className="brand" href="#/login">
          <span className="brand-mark">C</span>
          <span>CINESHELF</span>
        </a>
        <span className="header-tag">YOUR MOVIES</span>
      </header>

      <div className="auth-layout">
        <section className="intro">
          <p className="eyebrow">A LITTLE MORE PERSONAL</p>
          <h2>Your shelf.<br /><span>Your stories.</span></h2>
          <p className="intro-copy">
            Sign in to browse your CineShelf, organise your collection, and plan your next movie night.
          </p>
          <div className="learning-points">
            <p><span>01</span> Your account is protected by a JWT</p>
            <p><span>02</span> Search and filter your movie collection</p>
            <p><span>03</span> Add, edit, and manage your movies</p>
          </div>
        </section>
        <LoginForm onLogin={handleLogin} />
      </div>

      <footer className="auth-footer">
        <span>BUILT FOR MOVIE LOVERS</span>
        <span>YOUR PERSONAL MOVIE LIBRARY</span>
      </footer>
    </main>
  )
}

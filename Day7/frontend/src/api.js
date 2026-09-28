const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })

  if (!response.ok) {
    const result = await response.json().catch(() => ({}))
    throw new Error(result.detail || 'The request could not be completed.')
  }

  if (response.status === 204) return null
  return response.json()
}

export function getMovies({ search = '', genre = '', signal } = {}) {
  const params = new URLSearchParams()
  if (search.trim()) params.set('search', search.trim())
  if (genre) params.set('genre', genre)
  const query = params.toString()
  return request(`/movies${query ? `?${query}` : ''}`, { signal })
}

export function getGenres() {
  return request('/genres')
}

export function getMovie(movieId) {
  return request(`/movies/${movieId}`)
}

export function createMovie(movie) {
  return request('/movies', {
    method: 'POST',
    body: JSON.stringify(movie),
  })
}

export function updateMovie(movieId, movie) {
  return request(`/movies/${movieId}`, {
    method: 'PUT',
    body: JSON.stringify(movie),
  })
}

export function setWatched(movieId, watched) {
  return request(`/movies/${movieId}/watched`, {
    method: 'PATCH',
    body: JSON.stringify({ watched }),
  })
}

export function deleteMovie(movieId) {
  return request(`/movies/${movieId}`, { method: 'DELETE' })
}
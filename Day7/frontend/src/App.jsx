import { useEffect, useState } from 'react'
import { Film, Star } from 'lucide-react'
import * as api from './api.js'
import Navbar from './components/Navbar.jsx'
import MovieForm from './components/MovieForm.jsx'
import MovieList from './components/MovieList.jsx'
import MovieDetails from './components/MovieDetails.jsx'

export default function App() {
  const [movies, setMovies] = useState([])
  const [genres, setGenres] = useState([])
  const [search, setSearch] = useState('')
  const [genre, setGenre] = useState('')
  const [selectedMovie, setSelectedMovie] = useState(null)
  const [editingMovie, setEditingMovie] = useState(null)
  const [formOpen, setFormOpen] = useState(false)
  const [loading, setLoading] = useState(true)
  const [apiOnline, setApiOnline] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    const controller = new AbortController()
    setLoading(true)
    api.getMovies({ search, genre, signal: controller.signal })
      .then((results) => {
        setMovies(results)
        setApiOnline(true)
        setError('')
      })
      .catch((loadError) => {
        if (loadError.name !== 'AbortError') {
          setError('Could not reach the API. Start the FastAPI server, then refresh.')
          setApiOnline(false)
        }
      })
      .finally(() => setLoading(false))
    return () => controller.abort()
  }, [search, genre])

  useEffect(() => {
    api.getGenres().then(setGenres).catch(() => {})
  }, [movies.length])

  async function refreshMovies() {
    const results = await api.getMovies({ search, genre })
    setMovies(results)
    setGenres(await api.getGenres())
  }

  async function saveMovie(movieData) {
    const savedMovie = editingMovie
      ? await api.updateMovie(editingMovie.id, movieData)
      : await api.createMovie(movieData)
    await refreshMovies()
    setSelectedMovie(savedMovie)
    setFormOpen(false)
    setEditingMovie(null)
  }

  async function toggleWatched(movie) {
    try {
      const updatedMovie = await api.setWatched(movie.id, !movie.watched)
      setSelectedMovie(updatedMovie)
      await refreshMovies()
    } catch (requestError) {
      setError(requestError.message)
    }
  }

  async function removeMovie(movie) {
    if (!window.confirm(`Delete “${movie.title}” from your collection?`)) return
    try {
      await api.deleteMovie(movie.id)
      setSelectedMovie(null)
      await refreshMovies()
    } catch (requestError) {
      setError(requestError.message)
    }
  }

  function openEditForm(movie) {
    setEditingMovie(movie)
    setSelectedMovie(null)
    setFormOpen(true)
  }

  const watchedCount = movies.filter((movie) => movie.watched).length
  const averageRating = movies.length
    ? (movies.reduce((total, movie) => total + movie.rating, 0) / movies.length).toFixed(1)
    : '—'

  return (
    <div id="top" className="app-shell">
      <Navbar
        search={search}
        onSearchChange={setSearch}
        genres={genres}
        genre={genre}
        onGenreChange={setGenre}
        onAddMovie={() => { setEditingMovie(null); setFormOpen(true) }}
        apiOnline={apiOnline}
      />

      <main>
        <section className="intro-band">
          <div className="intro-copy">
            <p className="eyebrow">A LITTLE PLACE FOR YOUR MOVIES</p>
            <h1>Your next<br /><span>favorite rewatch.</span></h1>
            <p className="intro-caption">A considered collection of films, all in one place.</p>
          </div>
          <div className="intro-art" aria-hidden="true">
            <div className="ticket ticket-back"><span>ADMIT ONE</span><Film size={31} /></div>
            <div className="ticket ticket-front"><span>TONIGHT'S PICK</span><Star size={26} fill="currentColor" /><b>MAKE IT<br />A MOVIE NIGHT</b></div>
            <span className="intro-number">01—05</span>
          </div>
        </section>

        <section className="collection-section" aria-labelledby="collection-title">
          <div className="stats-row">
            <div className="section-title-wrap">
              <p className="eyebrow">YOUR PERSONAL ARCHIVE</p>
              <h2 id="collection-title">The collection</h2>
            </div>
            <div className="stats-group">
              <div className="stat"><strong>{movies.length}</strong><span>films</span></div>
              <div className="stat"><strong>{watchedCount}</strong><span>watched</span></div>
              <div className="stat"><strong>{averageRating}</strong><span>avg. rating</span></div>
            </div>
          </div>

          {error && <div className="error-banner" role="alert">{error}</div>}
          <MovieList
            movies={movies}
            loading={loading}
            search={search}
            genre={genre}
            onSelect={setSelectedMovie}
            onToggleWatched={toggleWatched}
          />
        </section>
      </main>

      <footer className="page-footer"><span>REEL LIST</span><span>Made for the love of film.</span></footer>

      {formOpen && (
        <MovieForm
          key={editingMovie?.id || 'new'}
          movie={editingMovie}
          onSave={saveMovie}
          onClose={() => { setFormOpen(false); setEditingMovie(null) }}
        />
      )}
      <MovieDetails
        movie={selectedMovie}
        onClose={() => setSelectedMovie(null)}
        onEdit={openEditForm}
        onDelete={removeMovie}
        onToggleWatched={toggleWatched}
      />
    </div>
  )
}
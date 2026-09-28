import { Clapperboard } from 'lucide-react'
import MovieCard from './MovieCard.jsx'

export default function MovieList({ movies, loading, search, genre, onSelect, onToggleWatched }) {
  if (loading) return <div className="list-message">Loading your collection…</div>

  if (movies.length === 0) {
    return (
      <div className="empty-state">
        <Clapperboard size={34} strokeWidth={1.5} />
        <h2>{search || genre ? 'No movies match those filters' : 'Your collection is waiting'}</h2>
        <p>{search || genre ? 'Try another title or genre.' : 'Add a movie to start your collection.'}</p>
      </div>
    )
  }

  return (
    <div className="movie-grid">
      {movies.map((movie) => (
        <MovieCard
          key={movie.id}
          movie={movie}
          onSelect={onSelect}
          onToggleWatched={onToggleWatched}
        />
      ))}
    </div>
  )
}
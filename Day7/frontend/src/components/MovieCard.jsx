import { Check, Circle, Star } from 'lucide-react'

export default function MovieCard({ movie, onSelect, onToggleWatched }) {
  return (
    <article className="movie-card">
      <button className="poster-button" onClick={() => onSelect(movie)} aria-label={`View ${movie.title}`}>
        <div className="poster-art">
          {movie.poster_url && (
            <img
              className="poster-image"
              src={movie.poster_url}
              alt={`${movie.title} poster`}
              loading="lazy"
              onError={(event) => { event.currentTarget.style.display = 'none' }}
            />
          )}
          <span className="poster-fallback" aria-hidden="true">{movie.title}</span>
          <span className="poster-rating"><Star size={13} fill="currentColor" /> {movie.rating.toFixed(1)}</span>
          <span className="poster-open">View details</span>
        </div>
      </button>
      <div className="movie-card-info">
        <div className="movie-card-heading">
          <button className="movie-title" onClick={() => onSelect(movie)}>{movie.title}</button>
          <button
            className={`watched-toggle ${movie.watched ? 'is-watched' : ''}`}
            onClick={() => onToggleWatched(movie)}
            title={movie.watched ? 'Mark as unwatched' : 'Mark as watched'}
            aria-label={movie.watched ? `Mark ${movie.title} as unwatched` : `Mark ${movie.title} as watched`}
          >
            {movie.watched ? <Check size={15} /> : <Circle size={15} />}
          </button>
        </div>
        <p className="movie-card-meta">{movie.genre}<span>·</span>{movie.release_year}</p>
      </div>
    </article>
  )
}
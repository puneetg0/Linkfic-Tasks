import { Check, Clock3, Pencil, Star, Trash2, X } from 'lucide-react'

export default function MovieDetails({ movie, onClose, onEdit, onDelete, onToggleWatched }) {
  if (!movie) return null

  return (
    <div className="modal-backdrop" onMouseDown={(event) => event.target === event.currentTarget && onClose()}>
      <section className="modal-panel details-panel" role="dialog" aria-modal="true" aria-labelledby="details-title">
        <button className="icon-button details-close" onClick={onClose} title="Close" aria-label="Close details"><X size={20} /></button>
        <div className="details-poster">
          {movie.poster_url && <img src={movie.poster_url} alt={`${movie.title} poster`} onError={(event) => { event.currentTarget.style.display = 'none' }} />}
          <span className="poster-fallback" aria-hidden="true">{movie.title}</span>
        </div>
        <div className="details-copy">
          <p className="eyebrow">MOVIE DETAILS</p>
          <h2 id="details-title">{movie.title}</h2>
          <p className="details-meta">{movie.genre}<span>·</span>{movie.release_year}</p>
          <div className="detail-rating"><Star size={17} fill="currentColor" /> <strong>{movie.rating.toFixed(1)}</strong><span>/ 10</span></div>
          <div className={`watch-status ${movie.watched ? 'is-watched' : ''}`}>
            {movie.watched ? <Check size={16} /> : <Clock3 size={16} />}
            {movie.watched ? 'Watched' : 'On your watchlist'}
          </div>
          <div className="details-actions">
            <button className="button button-add" onClick={() => onToggleWatched(movie)}>
              {movie.watched ? <Clock3 size={16} /> : <Check size={16} />}
              {movie.watched ? 'Mark unwatched' : 'Mark watched'}
            </button>
            <button className="button button-quiet" onClick={() => onEdit(movie)}><Pencil size={15} />Edit</button>
            <button className="button button-danger" onClick={() => onDelete(movie)}><Trash2 size={15} />Delete</button>
          </div>
        </div>
      </section>
    </div>
  )
}
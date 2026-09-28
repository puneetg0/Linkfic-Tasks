import { useState } from 'react'
import { X } from 'lucide-react'

export default function MovieForm({ movie, onSave, onClose }) {
  const [form, setForm] = useState({
    title: movie?.title || '',
    genre: movie?.genre || '',
    release_year: movie?.release_year || new Date().getFullYear(),
    rating: movie?.rating ?? 7,
    watched: movie?.watched ?? false,
    poster_url: movie?.poster_url || '',
  })
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

  function updateField(event) {
    const { name, value, checked, type } = event.target
    setForm({ ...form, [name]: type === 'checkbox' ? checked : value })
  }

  async function handleSubmit(event) {
    event.preventDefault()
    setSaving(true)
    setError('')
    try {
      await onSave({
        ...form,
        title: form.title.trim(),
        genre: form.genre.trim(),
        release_year: Number(form.release_year),
        rating: Number(form.rating),
        poster_url: form.poster_url.trim() || null,
      })
    } catch (saveError) {
      setError(saveError.message)
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="modal-backdrop" onMouseDown={(event) => event.target === event.currentTarget && onClose()}>
      <section className="modal-panel form-panel" role="dialog" aria-modal="true" aria-labelledby="form-title">
        <div className="modal-heading">
          <div>
            <p className="eyebrow">YOUR LIBRARY</p>
            <h2 id="form-title">{movie ? 'Edit movie' : 'Add a movie'}</h2>
          </div>
          <button className="icon-button" onClick={onClose} title="Close" aria-label="Close form"><X size={20} /></button>
        </div>
        <form className="movie-form" onSubmit={handleSubmit}>
          <label className="field field-wide">
            <span>Movie title</span>
            <input name="title" value={form.title} onChange={updateField} required maxLength="120" autoFocus />
          </label>
          <label className="field">
            <span>Genre</span>
            <input name="genre" value={form.genre} onChange={updateField} required maxLength="40" placeholder="e.g. Sci-Fi" />
          </label>
          <label className="field">
            <span>Release year</span>
            <input name="release_year" type="number" min="1888" max="2100" value={form.release_year} onChange={updateField} required />
          </label>
          <label className="field">
            <span>Rating <small>out of 10</small></span>
            <input name="rating" type="number" min="0" max="10" step="0.1" value={form.rating} onChange={updateField} required />
          </label>
          <label className="field field-wide">
            <span>Poster image URL <small>optional</small></span>
            <input name="poster_url" type="url" value={form.poster_url} onChange={updateField} placeholder="https://…" />
          </label>
          <label className="checkbox-field field-wide">
            <input name="watched" type="checkbox" checked={form.watched} onChange={updateField} />
            <span>I've watched this movie</span>
          </label>
          {error && <p className="form-error field-wide" role="alert">{error}</p>}
          <div className="form-actions field-wide">
            <button type="button" className="button button-quiet" onClick={onClose}>Cancel</button>
            <button type="submit" className="button button-add" disabled={saving}>
              {saving ? 'Saving…' : movie ? 'Save changes' : 'Add to collection'}
            </button>
          </div>
        </form>
      </section>
    </div>
  )
}
import { Film, Plus, Search } from 'lucide-react'

export default function Navbar({
  search,
  onSearchChange,
  genres,
  genre,
  onGenreChange,
  onAddMovie,
  apiOnline,
}) {
  return (
    <header className="topbar">
      <a className="brand" href="#top" aria-label="Reel List home">
        <span className="brand-mark"><Film size={19} strokeWidth={2.4} /></span>
        <span>reel<span className="brand-light">list</span></span>
      </a>

      <div className="topbar-tools">
        <label className="search-box">
          <Search size={17} aria-hidden="true" />
          <span className="visually-hidden">Search movies</span>
          <input
            value={search}
            onChange={(event) => onSearchChange(event.target.value)}
            placeholder="Search your collection"
          />
        </label>
        <label className="genre-control">
          <span className="visually-hidden">Filter by genre</span>
          <select value={genre} onChange={(event) => onGenreChange(event.target.value)}>
            <option value="">All genres</option>
            {genres.map((item) => <option key={item} value={item}>{item}</option>)}
          </select>
        </label>
        <button className="button button-add" onClick={onAddMovie}>
          <Plus size={17} />
          <span>Add a movie</span>
        </button>
      </div>
      <span className={`connection ${apiOnline ? 'online' : ''}`} title={apiOnline ? 'API connected' : 'Connecting to API'}>
        <span className="connection-dot" />
        <span>{apiOnline ? 'Connected' : 'Connecting'}</span>
      </span>
    </header>
  )
}
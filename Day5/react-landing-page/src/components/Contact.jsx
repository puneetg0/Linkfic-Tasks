function Contact() {
  function handleSubmit(event) {
    event.preventDefault();
    alert("Thank you! Your message has been submitted.");
  }

  return (
    <section className="section" id="contact">
      <div className="container contact-content">
        <p className="eyebrow">Contact</p>
        <h2>Let's Work Together</h2>
        <p>Have a question? Send us a message.</p>

        <form className="contact-form" onSubmit={handleSubmit}>
          <input type="text" placeholder="Your Name" required />
          <input type="email" placeholder="Your Email" required />
          <textarea placeholder="Your Message" rows="5" required />
          <button className="button" type="submit">Send Message</button>
        </form>
      </div>
    </section>
  );
}

export default Contact;
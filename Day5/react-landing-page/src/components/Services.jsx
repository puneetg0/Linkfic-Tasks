const services = [
  {
    title: "Web Development",
    description: "Build responsive and modern websites for different devices."
  },
  {
    title: "React Development",
    description: "Create reusable components and interactive React applications."
  },
  {
    title: "UI Design",
    description: "Create clean and user-friendly interfaces with HTML and CSS."
  }
];

function Services() {
  return (
    <section className="section services-section" id="services">
      <div className="container">
        <p className="eyebrow">Services</p>
        <h2>What We Do</h2>

        <div className="service-container">
          {services.map((service) => (
            <article className="service-card" key={service.title}>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
              <a href="#contact">Learn More</a>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Services;
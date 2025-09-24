import Link from 'next/link';

const Home = () => {
  return (
    <div className="bg-gradient-to-r from-purple-800 via-black to-purple-800 text-gray-300 w-full min-h-screen flex flex-col">
      {/* Navigation */}
      <nav className="flex justify-between items-center p-5 border-b-1 border-purple-800 bg-black text-gray-300">
        <div className="flex gap-4">
        <Link href="/"><strong>Home</strong></Link>
        <a
      href="https://github.com/ChrIs8279"
      target="_blank"
      rel="noopener noreferrer"
      className="text-gray-300"
      >
        GitHub
      </a>
      </div>
        <div className="flex gap-4">
          <Link href = "/resume">My Resume</Link>
          <Link href="/contact">Contact Me</Link>
          <Link href="/about">About Me</Link>
          <Link href="/projects">My Skills</Link>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero-section text-center bg-gradient-to-r from-purple-800 via-black to-purple-800 text-gray-300 py-10">
        <h1 className="text-6xl font-bold mb-4">Christopher Clendenning</h1>
        <p className="text-xl">Coding, Automation, Websites, and Retail For Hire</p>
      </section>
      <section className="Content mx-auto mt-5 mb-10">
      <div>

      {/* Projects Section */}
      <section className="projects text-center mt-5 mb-8 text-gray-300 w-full">
        <h2 className="text-3xl font-semibold mb-4">My Skill Set</h2>
        <p className="text-lg max-w-xl mx-auto mb-6">
          Here's what I can do for you!
        </p>
        <section className = "justify-center mb-3">
        <Link href="/projects">
          <button className="hover:shadow-purple-500/50 w-60 text-gray-300 py-2 px-10 rounded-md border-2 border-black-900 transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg">
            My Skills
          </button>
          </Link>
          </section>
          <section className = "justify-center mt-3">
          <Link href="/blog">
          <button className = "hover:shadow-purple-500/50 w-60 text-gray-300 py-2 px-10 rounded-md border-2 border-black-900 transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg">
          Blog
          </button>
        </Link>
        </section>
      </section>

      {/* Contact Section */}
      <section className="contact text-center mt-5 text-gray-300">
        <h2 className="text-3xl font-semibold mb-4">Contact Me</h2>
        <p className="text-lg max-w-xl mx-auto mb-6">
          Have a Question? Contact me Here!
        </p>
        <Link href="/contact">
          <button className="hover:shadow-purple-500/50 w-60 text-gray-300 py-2 px-10 rounded-md border-2 border-black-900 transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg">
            Contact Me
          </button>
        </Link>
      </section>
      </div>
      </section>

      <section className="intro text-center mt-1 mb-8 text-gray-300 bg-gradient-to-r from-purple-800 via-black to-purple-800">
        <h2 className="text-3xl font-semibold mb-4">About Me</h2>
        <p className="text-lg max-w-xl mx-auto mb-6">
          Hi! Since You're Already Here, Why Not Get to Know me?
        </p>
        <div className="justify-center mb-3">
        <Link href="/about">
          <button className="hover:shadow-purple-500/50 w-60 text-gray-300 py-2 px-10 rounded-md border-2 border-black-900 transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg">
            Learn More About Me
          </button>
        </Link>
        <div className="justify-center mt-3">
        <Link href="/resume">
          <button className="hover:shadow-purple-500/50 w-60 text-gray-300 py-2 px-10 rounded-md border-2 border-black-900 transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg"> General Resume
          </button>
        </Link>
        </div>
        </div>
      </section>
      

      {/* Footer Section */}
      <footer className="text-center text-gray-300 py-8 bg-black border-t-1 border-purple-800">
        <p>© 2025 Christopher Clendenning | All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Home;

import React from 'react'

// const Hero = (props) => {
// Instead of props we can use like below then we can simply use title and subtitle.
//  We can use default props content like below or simple {title, subtitle}
const Hero = ({title='Became a React dev ', subtitle='Find the React Jobs that fits your skill set'}) => {
  return (
    <section className="bg-indigo-700 py-20 mb-4">
      <div
        className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center"
      >
        <div className="text-center">
          <h1
            className="text-4xl font-extrabold text-white sm:text-5xl md:text-6xl"
          >
            {/* Become a React Dev */}
            {/* Instead of hard coded we can use like below  */}
            {/* { props.title} */}
            {/* If we don't use props then use like below */}
            { title }
          </h1>
          <p className="my-4 text-xl text-white">
            {/* Find the React job that fits your skills and needs */}
            {/* { props.subtitle } */}
            { subtitle }
          </p>
        </div>
      </div>
    </section>
  )
}

export default Hero
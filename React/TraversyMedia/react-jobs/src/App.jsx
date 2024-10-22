// ````````````````````````` Start Home Page '''''''''''''''''''''''''''''''


import React from 'react'
import Navbar from '../src/components/Navbar';
import Hero from './components/Hero';
import HomeCards from './components/HomeCards';
import JobListings from './components/JobListings';
import ViewAllJobs from './components/viewAllJobs';


const App = () => {
  return (
    <>
      <Navbar />
      {/* We can use like just below line too  */}
      {/* <Hero title='Test Title' subtitle='This is the subtitle' /> */}
         { /* if we use default then don't need to mention here  */}
      <Hero />
      <HomeCards />
      <JobListings />
      <ViewAllJobs />
    </>
  )
}

export default App


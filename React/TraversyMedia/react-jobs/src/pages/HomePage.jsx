import React from 'react';
import Hero from '../components/Hero';
import HomeCards from '../components/HomeCards';
import JobListings from '../components/JobListings';
import ViewAllJobs from '../components/viewAllJobs';


const HomePage = () => {
  return (
    <>
        <Hero />
        <HomeCards />
        <JobListings />
        <ViewAllJobs />
    </>
  )
}

export default HomePage
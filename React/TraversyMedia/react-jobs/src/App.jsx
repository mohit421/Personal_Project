// ````````````````````````` Start Home Page '''''''''''''''''''''''''''''''

import { 
  Route, 
  createBrowserRouter, 
  createRoutesFromElements,
  RouterProvider,
} from 'react-router-dom';
import React from 'react';

import HomePage from './pages/HomePage'
import MainLayout from './layouts/MainLayout';
import JobPage from './pages/JobPage';

const router = createBrowserRouter(
  createRoutesFromElements(
    // <Route index element={<h1>Welcome to My App</h1>} />)
    <Route path='/' element={<MainLayout />}>
      <Route index element={<HomePage />} />
      <Route path='/jobs' element={<JobPage />} />
    </Route>
  )
    // <Route path='/about' element={<h1>Welcome to My App</h1>} />)
    // (
    // <>
    // <Navbar />
    // {/* We can use like just below line too  */}
    // {/* <Hero title='Test Title' subtitle='This is the subtitle' /> */}
    //    { /* if we use default then don't need to mention here  */}
    // <Hero />
    // <HomeCards />
    // <JobListings />
    // <ViewAllJobs />
    // </>
  // )
);

const App = () => {
  return <RouterProvider router={router} />;
  
};

export default App


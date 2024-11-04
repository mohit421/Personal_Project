import { 
  Route, 
  createBrowserRouter, 
  createRoutesFromElements,
  RouterProvider,
} from 'react-router-dom';
import React from 'react';

import HomePage from './pages/HomePage'
import MainLayout from './layouts/MainLayout';
import JobsPage from './pages/JobsPage';
import JobPage, {jobLoader } from './pages/JobPage';
import NotFoundPage from './pages/NotFoundPage';
import AddJobPage from './pages/AddJobPage';


const router = createBrowserRouter(
  createRoutesFromElements(
    // <Route index element={<h1>Welcome to My App</h1>} />)
    <Route path='/' element={<MainLayout />}>
      <Route index element={<HomePage />} />
      <Route path='/jobs' element={<JobsPage />} />
      <Route path='/add-job' element={<AddJobPage />} />
      <Route path='/jobs/:id' element={<JobPage />} loader={jobLoader} />
      {/* Any page that not found we just go there */}
      <Route path='*' element={<NotFoundPage />} />
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


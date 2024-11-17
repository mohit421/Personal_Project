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
import EditJobPage from './pages/EditJobPage';


const App = () => {
  // Add new job 
  const addJob =async (newJob) => {
    // console.log(newJob);
    const res = await fetch('/api/jobs', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newJob)
    });
    return;
}
// Delete Job
const deleteJob = async (id) => {
  // console.log('delete', id);
    const res = await fetch(`/api/jobs/${id}`, {
      method: 'DELETE',
    });
    return;
}

// Update Job

const updateJob = async (job) => {
  // console.log(newJob);
  const res = await fetch(`/api/jobs/${job.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(job)
  });
  return;
}

const router = createBrowserRouter(
  createRoutesFromElements(
    // <Route index element={<h1>Welcome to My App</h1>} />)
    <Route path='/' element={<MainLayout />}>
      <Route index element={<HomePage />} />
      <Route path='/jobs' element={<JobsPage />} />
      <Route path='/add-job' element={<AddJobPage addJobSubmit={addJob} />} />
      <Route path='/jobs/:id' element={<JobPage deleteJob = {deleteJob}/>} loader={jobLoader} />
      <Route path='/edit-job/:id' 
      element={<EditJobPage updatedJobSubmit = {updateJob} />} 
      loader={jobLoader} />
      
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

  return <RouterProvider router={router} />;
  
};

export default App;


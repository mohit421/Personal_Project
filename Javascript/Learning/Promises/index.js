// -> Four Promises API that are majorly important
//  1. Promise.all():- 
//      It waits for all of the promises to finish.Then returns an array with all value of promises
//  What if any of the promises get rejected?
//      It will throws an error immediately asa soon as it will get an error.

//  How much time it will take?
//       Let say promise.all([p1,p2,p3]) takes 3s, 2s, and 1s respectively. Then it will give result in 3 sec if all promises resolve.
//      Let say p2 fails in 2s then we will get error in 2s that p2 fail otherwise if p3 fails then we will get res in 1 sec that p3 fails. and it will not wait for other promises to settle after failure.



//  2. Promise.allSettled():-
//      Wait for all the promises to settled (i.e., resolve or reject)
//      Let say Promise.allSettled([p1,p2,p3]) takes 3s, 1s, and 2s.
//      If all promises are resolved then it will return an object of all promises.
//  What if p2 gets rejected?
//      Still it will waits for all promises to settled then it will give result. it will give results in 2 sec.
//  Promise.all() is kind of failed quickly than Promise.allSettled()


// 3. Promise.race():-
//      We will get the result of first settled promise.
//      Let say Promise.race([p1,p2,p3]) takes 3s, 1s, and 2s. 
//      if all promises are resolved then we will get result of p2 success only.
//      if all promises are rejected then we will get error of p2 fail only.
//      we will get the result of first settled(success or failure doesn't matter) whether it got rejected or resolved.
//      Return an single value 


// 3. Promise.any():-
//      It is very much similar to race() API.
//      But only difference is that it will wait for 1st promise to gets successful. Wait for first fullfil/success.
//      Let say Promise.race([p1,p2,p3]) takes 3s, 1s, and 2s. 
//      if all promises are resolved then we will get result of p2 success only.
//      if all promises are rejected/fails then we will get AggregateError: array of all three promises  -> [err1,err2,err3]
//      if p2 fails and p1 and p3 success then we will get p3 success as our result only in 2s.
//      if p2 and p3 fails and p1 success then it will give result in 3 sec as p1 success.
//      Seeking for first success.
//      



// promise.all takes an array of promises as input and makes parallel API calls.
// If any promise in the Promise.all array gets rejected, the Promise.all will throw an error, and the same error will be the output
// The Promise APIs all and allSettled handle the success and failure of multiple promises.
// In a race between multiple promises, the first promise to settle (either resolve or reject) will determine the result.
// Promise.any waits for the first successful promise.  If all promises fail, an aggregated error will be returned.



const p1 = new Promise((resolve,reject)=>{
    // setTimeout(()=> resolve("P1 Success"),3000);
    setTimeout(()=> reject("P1 fail"),3000);
})


const p2 = new Promise((resolve,reject)=>{
    // setTimeout(()=> resolve("P2 success"),1000);
    setTimeout(()=> reject("P2 Fail"),1000);
    // setTimeout(()=> reject("P2 Fail"),1000);
})

const p3 = new Promise((resolve,reject)=>{
    // setTimeout(()=> resolve("P3 Success"),2000);
    // setTimeout(()=> resolve("P3 Success"),2000);
    setTimeout(()=> reject("P3 Fail"),2000);
})
//                                      1.  Promise.all()
// expample-1:

// Promise.all([p1,p2,p3]).then((res) => {
//     console.log(res);
// })

// example-2

Promise.all([p1,p2,p3])
    .then((res) => {
        console.log(res);
    })
    .catch((err)=>{
        console.error(err);
    });


//                                      1.  Promise.allSettled()

// Promise.allSettled([p1,p2,p3])
//     .then((res) => {
//         console.log(res);
//     })
//     .catch((err)=>{
//         console.error(err);
//     });


//                                      1.  Promise.race()

// Promise.race([p1,p2,p3])
//     .then((res) => {
//         console.log(res);
//     })
//     .catch((err)=>{
//         console.error(err);
//     });

//                                      1.  Promise.any()

// Promise.any([p1,p2,p3])
//     .then((res) => {
//         console.log(res);
//     })
//     .catch((err)=>{
//         console.error(err);
//     });

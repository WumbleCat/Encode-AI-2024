import Moralis from 'moralis';
try {
  await Moralis.start({
    apiKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImZlMjM4NDA4LWYyYWItNDVkOC05OTJmLTczNzA2ZDczOTg1NCIsIm9yZ0lkIjoiMzgxOTQ4IiwidXNlcklkIjoiMzkyNDYyIiwidHlwZUlkIjoiNTJkYmEyNTUtYzkwNy00NmM2LWE1MjktZGE3ZDU0MmQyMzdlIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MDk5NzY3MjIsImV4cCI6NDg2NTczNjcyMn0.tN_qq1E-UhQdJwMIxwmORaIABNtRERVUnfWSIiwe5iw"
  });

  const response = Moralis.Auth.requestMessage({});
  console.log(response.raw);
} catch (e) {
  console.error(e);
}
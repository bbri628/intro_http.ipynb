7. **Document Your Experience**  
   See screenshots showing:
   - The server terminal with logged request details.
   - The output of a curl command (or browser view) displaying the server’s response.
  
  ![httpworld](https://github.com/user-attachments/assets/25dc6a8f-b4aa-4493-a74a-174d3c9e9a74)
![http1](https://github.com/user-attachments/assets/2a673b5b-678d-4fc4-b11f-947c31f7f552)
![getpost](https://github.com/user-attachments/assets/86d5a197-ef1a-426f-8739-bf91ed67cb07)
![custom server](https://github.com/user-attachments/assets/2cd36807-a6d5-45dd-bc63-cd6df8e07e70)
 

9. **Reflection**  
   In your notes or a short write-up, answer:
   - What does the server log when a GET vs. a POST request is made?
    GET: A request to retrieve data from the server eg. (Fetching a list of users,Loading a webpage, Getting a product’s details)
    POST: Send data to the server to create or update something. eg. (Submitting a form, Creating a new user, Posting a blog article)

   - How do HTTP methods (GET and POST) differ in how data is sent and received?
     
GET	
URL query string (?key=value)	
Visible in browser address bar	
Less secure for sensitive data	
Read/fetch data	
Data Size Limit	Smaller (URL length)	

POST
Request body
Hidden from URL
Better for sensitive data
Submit/create data
Larger (server-dependent)

 - What HTTP status code did your server return, and what does it signify?
POST request received! (HTTP status code 200 which means the server successfully handled the POST request.)

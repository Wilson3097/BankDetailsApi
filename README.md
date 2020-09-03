# BankDetailsApi
  This is a restful service to fetch the bank details from the IFSC code, name of the bank and city.
  I have also implemented django import export feature so that all the bank details can be directly 
  uploaded in bulk via admin. I have uploaded the details using that only. I have uploaded around 500k bank details using import feature directly and have tested all the apis on the data.
  
  ## Installation
      Use the following command: "pip install -r requirements.txt" to install all the requirements.
      Use postman to test all the apis.
   
  
  
 ## APIs Documentation
    You can run it on localhost.
    For eg  localhost/bank/getDetailsFromIFSC/
    All the APIs have been tested on Postman and are working perfectly fine.
    I have handled the edge cases if the bank is not present.
    
    Postman
        Body for the getDetailsFromIFSC/ api is 
            "ifsc":"any ifsc code you want to query"
        Body for the getDetailsFromNameCity/ api is
            "name":"BankName"
            "city":"City Name"

   ### Bank Details endpoints

   <table>
   	<tr>
   		<th>S.No.</th>
   		<th>Route</th>
   		<th>Method</th>
   		<th>Access</th>
   		<th>Description</th>
   	</tr>
   	<tr>
           <td>1.</td>
           <td>bank/getDetailsFromIFSC/</td>
           <td>POST</td>
           <td>public</td>
           <td>search details from IFSC</td>
       </tr>
   	 <tr>
           <td>2.</td>
           <td>bank/getDetailsFromNameCity/</td>
           <td>POST</td>
           <td>public</td>
           <td>search details from name and city</td>
       </tr>
  <tr>
           <td>3.</td>
           <td>bank/crudBank/</td>
           <td>GET</td>
           <td>public</td>
           <td>returns all the bank details</td>
       </tr>
  <tr>
           <td>3.</td>
           <td>bank/crudBank/</td>
           <td>POST</td>
           <td>public</td>
           <td>creates a bank</td>
       </tr>
  <tr>
           <td>3.</td>
           <td>bank/crudBank/1/</td>
           <td>GET</td>
           <td>public</td>
           <td>returns a particular bank details</td>
       </tr>

  <tr>
           <td>3.</td>
           <td>bank/crudBank/1/</td>
           <td>PUT</td>
           <td>public</td>
           <td>Update bank details</td>
       </tr>
        <tr>
           <td>3.</td>
           <td>bank/crudBank/1/</td>
           <td>DELETE</td>
           <td>public</td>
           <td>Delete bank details</td>
       </tr>

   </table>


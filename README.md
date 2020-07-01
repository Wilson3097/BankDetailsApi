# BankDetailsApi
  This is a restful service to fetch the bank details from the IFSC code, name of the bank and city.
  
  ## Installation
      Use the following command: "pip install -r requirements.txt" to install all the requirements.
      Use postman to test all the apis.
   
   ## Deployment
       This app is deployed on heroku.
       The URL is credicxoapp.herokuapp.com
  
  
 ## APIs Documentation
    Use the above url as the base url and then the endpoints mentioned below to test in the postman.
    For eg  credicxoapp.herokuapp.com/bank/getDetailsFromIFSC/
    All the APIs have been tested on Postman and are working perfectly fine.
    For now I have uploaded the first 500 banks from the list of banks. 
    As free heroku server had its limitations. 
    So please while querying give any ifsc,name or city from the first 500 only. 
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
           <td>Get details from IFSC</td>
       </tr>
   	 <tr>
           <td>2.</td>
           <td>bank/getDetailsFromNameCity/</td>
           <td>POST</td>
           <td>public</td>
           <td>Get details from name and city</td>
       </tr>
   	 <tr>
           <td>3.</td>
           <td>bank/getAllBanks/</td>
           <td>GET</td>
           <td>public</td>
           <td>returns all the bank details</td>
       </tr>


   </table>


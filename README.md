1) LOGIN AND REGISTER 
Try to login with user “group4”
Then register user “group4”
Try to login group4 with wrong password -> See the message
Try to login group4 with right password 
Try to register group4 again, then the message group4 has already register display
Try to register another account user1. We will use on next part

2) ADDING PRODUCT
Login with group4
Choose product, type username, serial number (1001), date format with (YYYY-MM-DD)
Then submit and go back. Click F5 to refresh
Try to adding another product with serial number as similar as above (1001). See the message, the serial number is wrong, because the serial product number is unique, all of the products have different serial number.
Try to adding again with serial number 1002. Go back and refresh the page with F5

Login with user1
Try to adding any product with 1003, and 1004

Only normal user can view their own product, group4 can see own product and CANNOT view the product of user1.
 
3) CLAIM PRODUCT
Enter the exact information of the product you want to claim. If you type wrong information the program don’t allow to claim. For example, you buy (IPHONE, 1001, 2021-08-03), 
if you type wrong one of these information you will get the error message. Click F5 to refresh
When you claim product successful, try to reclaim this product again and you see the message “ONLY ONE TIME CLAIM”
Try to adding another product with exceed 2 years protection plan to check the program work like (CAMERA, 1003, 2015-08-03). Click F5 to refresh
Then you claim this product and the program reject user to claim the product.

4) ADMIN USER
ADMIN user can view all of the users, bought product, status of claimed, date time purchased …
ADMIN user allows or rejects the claim requirement from normal user.
To do that, admin should complete the modify form, then submit to server. If user has sent the claim request, admin will see the comment, and the claim status will be 1. Click F5 to refresh
If admin agree to claim, they can fix the comment to agree or something
If user don’t want to claim this product, admin can modify claim status back to 0 and delete comment. Click F5 to refresh
	

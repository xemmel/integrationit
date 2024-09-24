- Create a new *Resource Group*
- Create a new *Service Bus Namespace* (Appears just as *Service Bus*)
   - Give it a unique name
   - Under *Pricing tier* choose **Standard**
- Leave other settings and Click *Review + create* -> *Create*

- Once created goto your newly create *Service Bus Namespace*
  - *Entities/Queues*
    - click *+ Queue*
    - Give the queue a name and leave all other properties 
    - Click **Create**

 - Click the queue just created
 - Goto *Service Bus Explorer*
 - Click *Send Messages*
 - Type something in the **Body** and click *Send*
 - Go back to *Overview* and verify that *Message Counts Active* is now **1 MESSAGES**

 - Now let's receive/consume the message
 - Click on *Service Bus Explorer* again
   - Change **Peek Mode** to **Receive Mode**
   - Click *Receive messages*
   - Choose *ReceiveAndDelete*
   - Click *Receive*
   - Click on the message received and verify that the **Message Body** is the some as you typed earlier

 - Go back to *Overview* and verify that the queue is now empty (Message Counts active)

 ## Topics

 - Go back to your *Service Bus Namespace* using the *Breadcrums* at the top
 - Go to *Entities/Topics*
 - Create a new Topic, give it a name and leave all other properties
 - Click on the topic and use the *Service Bus Explorer* to submit a message as before
 - This message has disappered, since no subscribers are found
 - Click *+ Subscription*
   - Give the subscription a name (logall) and click **Create**
 - Submit another message
 - Back in *Overview* scroll the the button and verify that your subscription now have 1 message
 - Create another subscription (denmark)
 - click on the subscription
 - Scroll down and choose *+ Add filter*
   - Name the filter **denmark**
   - In the **SQL Filter textbox** write  **(country = 'DK')**
   - Click *Save changes*
 - Navigate back to the topic by clicking on the topic name in the breadcrums
 - Submit another message
 - Verify that *logall* got yet another message but *denmark* did not
 - Now submit a message with custom property *country = 'DK'*
   - In the *Service Bus Explorer* click *Send messages*
   - Fill in some content
   - Under **Custom Properties** click *+ Add custom property*
   - Set **Key** to *country*
   - Leave **Type** as *string*
   - Set **Value** to *DK*
   - Click *Send*
 - Now go back and verify that both subscriptions got the message


     


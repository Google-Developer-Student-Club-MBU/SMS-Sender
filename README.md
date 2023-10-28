import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class SMSApp {

    // Your Twilio Account SID and Auth Token
    private static final String ACCOUNT_SID = "Your_Account_SID";
    private static final String AUTH_TOKEN = "Your_Auth_Token";

    public static void main(String[] args) {
        // Initialize Twilio with your credentials
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);

        // Recipient's phone number and the message text
        String recipientPhoneNumber = "+1234567890"; // Replace with the recipient's phone number
        String messageText = "Hello, this is a test message from SMSApp.";

        // Send SMS
        try {
            Message message = Message.creator(
                    new PhoneNumber(recipientPhoneNumber),
                    new PhoneNumber("Your_Twilio_Phone_Number"), // Your Twilio phone number
                    messageText)
                    .create();

            System.out.println("SMS sent with SID: " + message.getSid());
            // Add code to update your progress bar and send a success notification here
        } catch (Exception e) {
            System.err.println("Error sending SMS: " + e.getMessage());
            // Add code to display an error notification here
        }
    }
}

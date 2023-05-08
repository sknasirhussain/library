import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.openqa.selenium.By;

public class Main {
    public static void main(String[] args) {
        // Set the path to the chromedriver executable
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");

        // Open the web browser and navigate to the website
        WebDriver driver = new ChromeDriver();
        driver.get("https://sknasirhussain.github.io/library/");

        // Find the text field and copy the data from the notepad file
        WebElement textField = driver.findElement(By.id("my-text-field"));
        try (BufferedReader br = new BufferedReader(new FileReader("Project text.txt"))) {
            String data = br.readLine();
            textField.sendKeys(data);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Submit the form or perform other actions as needed
        WebElement submitButton = driver.findElement(By.id("my-submit-button"));
        submitButton.click();

        // Close the browser
        driver.quit();
    }
}

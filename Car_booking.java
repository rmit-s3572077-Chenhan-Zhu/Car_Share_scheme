import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;
	import org.openqa.selenium.chrome.ChromeDriver;
	import org.openqa.selenium.support.ui.ExpectedConditions;
	import org.openqa.selenium.support.ui.WebDriverWait;
public class Car_booking {
	/**
	 //* @param args
	 */
	public static void main(String[]args) {

		System.setProperty("webdriver.chrome.driver",
				"/Users/mingmingmingming/Desktop/chromedriver");
				
//		 objects and variables instantiation
		WebDriver driver = new ChromeDriver();
		String appUrl = "http://www.wincarshare.tk";

		// launch the firefox browser and open the application url
		driver.get(appUrl);

		// maximize the browser window
		driver.manage().window().maximize();

		// declare and initialize the variable to store the expected title of
		// the webpage.
		String expectedTitle = "-WIN Rental";

		// fetch the title of the web page and save it into a string variable
		String actualTitle = driver.getTitle();

		// compare the expected title of the page with the actual title of the
		// page and print the result
		if (expectedTitle.equals(actualTitle)) {
			System.out.println("Verification Successful - The correct title is displayed on the web page.");
		} else {
			System.out.println("Verification Failed - An incorrect title is displayed on the web page.");
		}
		// click on the Booking button
		WebElement SignInButton = driver.findElement(By.name("booking"));
		SignInButton.click();
}
}
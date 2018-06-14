import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;
	import org.openqa.selenium.chrome.ChromeDriver;
	import org.openqa.selenium.support.ui.ExpectedConditions;
	import org.openqa.selenium.support.ui.WebDriverWait;
	import org.openqa.selenium.Alert;

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
		// enter a valid username in the email textbox
				WebElement username = driver.findElement(By.name("username"));
				username.clear();
				username.sendKeys("Abcd1234");

				WebDriverWait wait = new WebDriverWait(driver, 20);
		        wait.until(ExpectedConditions.presenceOfElementLocated(By.name("password")));
				// enter a valid password in the password textbox
				WebElement password = driver.findElement(By.name("password"));
				password.clear();
				password.sendKeys("Abcd1234");
				
			   // click on the login button
		      WebElement NextButton = driver.findElement(By.name("login"));
		      NextButton.click();
				
		      // click on the location button
		      WebElement MapButton = driver.findElement(By.name("gmimap0"));
		      MapButton.click();
		      
		      // click on the book button
		      WebElement LocationBookButton = driver.findElement(By.name("book"));
		      LocationBookButton.click();
		      
		      // enter a valid date in the pick up date picker 
		      WebElement month = driver.findElement(By.name("Bdatetime"));
		      month.clear();
		      month.sendKeys("Jul");
		      WebElement day = driver.findElement(By.name("Bday"));
		      day.clear();
		      day.sendKeys("1");
		      WebElement time = driver.findElement(By.name("Btime"));
		      time.clear();
		      time.sendKeys("09:30 AM");

		      // enter a valid date in the return date picker 
		      WebElement rmonth = driver.findElement(By.name("Rdatetime"));
		      rmonth.clear();
		      rmonth.sendKeys("Jul");
		      WebElement rday = driver.findElement(By.name("Rday"));
		      rday.clear();
		      rday.sendKeys("2");
		      WebElement rtime = driver.findElement(By.name("Rtime"));
		      rtime.clear();
		      rtime.sendKeys("09:30 AM");
		      
		      // click on the book now button
		      WebElement BookNowButton = driver.findElement(By.name("booknow"));
		      BookNowButton.click();
		      
		      //click confirm on alert
		      Alert javascriptAlert = driver.switchTo().alert();
		      javascriptAlert.accept();
		    //click confirm on alert
		      Alert javascriptAlerta = driver.switchTo().alert();
		      javascriptAlerta.accept();
		     
				// close the web browser
				//driver.close();
				System.out.println("Test script executed successfully.");

				// terminate the program
			}
		


}
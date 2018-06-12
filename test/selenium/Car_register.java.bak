import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;
	import org.openqa.selenium.chrome.ChromeDriver;
	import org.openqa.selenium.support.ui.ExpectedConditions;
	import org.openqa.selenium.support.ui.WebDriverWait;
	public class Car_register {

	

		/**
		 * @param args
		 */
		public static void main(String[]args) {

			System.setProperty("webdriver.chrome.driver",
					"/Users/mingmingmingming/Desktop/chromedriver");
//			 objects and variables instantiation
			WebDriver driver = new ChromeDriver();
			String appUrl = "http://www.wincarshare.tk/login/";
			// launch the firefox browser and open the application url
						driver.get(appUrl);

						// maximize the browser window
						driver.manage().window().maximize();

						// declare and initialize the variable to store the expected title of
						// the webpage.
						String expectedTitle = "Sign Up-WIN Rental";

						// fetch the title of the web page and save it into a string variable
						String actualTitle = driver.getTitle();

						// compare the expected title of the page with the actual title of the
						// page and print the result
						if (expectedTitle.equals(actualTitle)) {
							System.out.println("Verification Successful - The correct title is displayed on the web page.");
						} else {
							System.out.println("Verification Failed - An incorrect title is displayed on the web page.");
						}

						// click on the Sign Up button
						WebElement SignInButton = driver.findElement(By.name("register"));
						SignInButton.click();
						
						// enter a valid username in the email textbox
						WebElement username = driver.findElement(By.name("username"));
						username.clear();
						username.sendKeys("nick1");

						WebDriverWait wait = new WebDriverWait(driver, 20);
				        wait.until(ExpectedConditions.presenceOfElementLocated(By.name("password1")));
						// enter a valid password in the password textbox
						WebElement password1 = driver.findElement(By.name("password1"));
						password1.clear();
						password1.sendKeys("456");
						
						WebDriverWait wait1 = new WebDriverWait(driver, 20);
				        wait1.until(ExpectedConditions.presenceOfElementLocated(By.name("password2")));
						// enter a valid password in the password textbox
						WebElement password2 = driver.findElement(By.name("password2"));
						password2.clear();
						password2.sendKeys("456");
						// click on the Sign Up now button
						WebElement NextButton = driver.findElement(By.name("Sign Up now"));
			          	NextButton.click();
			// close the web browser
			//driver.close();
			System.out.println("Test script executed successfully.");

			// terminate the program
			
						

}
}
package gramcrackr.server.web;

import org.springframework.web.servlet.ModelAndView;
import gramcrackr.server.web.HelloController;
import junit.framework.TestCase;

public class HelloControllerTest extends TestCase {

	public void testHandleRequestView() throws Exception{
		HelloController controller = new HelloController();
		ModelAndView modelAndView = controller.handleRequest(null, null);
		assertEquals("hello.jsp", modelAndView.getViewName());
	}
}
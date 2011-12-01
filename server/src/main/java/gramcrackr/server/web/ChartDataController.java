package gramcrackr.server.web;

import java.io.IOException;

import java.io.PrintWriter;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import net.sf.json.JSONObject;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class ChartDataController implements Controller {
	
	protected ChartDataDAO dao;

	protected final Log logger = LogFactory.getLog(getClass());

	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//Cache cache = manager.getCache("sampleCache1");
		//cache.flush();
		response.addHeader("Access-Control-Allow-Origin","*");
		PrintWriter writer = response.getWriter();
		//writer.
		JSONObject json= new JSONObject();
		json.put("success", false);
		
		JSONObject jgrams= new JSONObject();
		
		Map<String, String[]> params=request.getParameterMap();
		
		String grams_str = params.get("grams")[0];
		String grams[];
		if (grams_str.contains(",")) {
			grams = grams_str.split(",");
		} else {
			grams = new String[1];
			grams[0] = grams_str;
		}
		for (String gram : grams) {
			gram = gram.replace(" ", "");
			//System.out.println(gram);
			jgrams.put(gram, dao.getNgramData(gram));
		}
		
		
		//String value=dao.getNgramData("php");
		//json.put("valueReturn", value);
		json.put("success", true);
		json.put("grams",jgrams);
		writer.print(json);
		return null;
	}
	
	public void setChartDataDAO(ChartDataDAO cdd) {
		this.dao=cdd;
	}

}

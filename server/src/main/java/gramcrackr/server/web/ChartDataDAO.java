package gramcrackr.server.web;

import org.iq80.leveldb.*;
import org.springframework.util.StringUtils;

import static org.fusesource.leveldbjni.JniDBFactory.*;
import java.io.*;

enum Dataset{StackOverflow};

public class ChartDataDAO{
	DB db[];


	public ChartDataDAO() throws IOException {
		System.out.println("Starting ChartDataDAO");

		db = new DB[4];
		System.out.println("Starting Databases");

		Options options = new Options();
		options.createIfMissing(true);
		for (int i=0; i<4; i++) {
			System.out.println("Starting DB for "+(i+1)+"-gram");
			db[i] = factory.open(new File("db-"+(i+1)+"grams"), options);
		}
	}

	public String getNgramData(String ngram) {
		int count = StringUtils.countOccurrencesOf(ngram," ");
		return asString(db[count].get(bytes(ngram)));
	}

}
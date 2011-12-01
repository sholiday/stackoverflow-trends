package gramcrackr.server.load;

import static org.fusesource.leveldbjni.JniDBFactory.factory;
import gramcrackr.server.web.ChartDataDAO;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import org.iq80.leveldb.*;
import static org.fusesource.leveldbjni.JniDBFactory.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		int n = 1;
		long grandTotal = 0;
		int localTotal = 0;
		int bufferCount = 10000;

		System.out.println("Importing");


		DB db;
		System.out.println("Starting Databases");

		Options options = new Options();
		options.createIfMissing(true);
		System.out.println("Starting DB for "+n+"-gram");
		db = factory.open(new File("db-"+n+"grams"), options);

		BufferedReader br = new BufferedReader(new FileReader("/Users/stephen/6_1gram_dates_by_gram"));
		String line;
		String []parts;


		WriteBatch batch = db.createWriteBatch();

		while ((line = br.readLine()) != null)   {
			// Print the content on the console


			parts = line.split("\t", 2);
			

			batch.put(bytes(parts[0]), bytes(parts[1]));
			
			grandTotal++;
			localTotal++;
			
			if (localTotal==bufferCount) {
				db.write(batch);
				batch.close();
				localTotal=0;
				System.out.println ("Stored "+grandTotal);
				batch = db.createWriteBatch();
			}
		}
		db.write(batch);
		batch.close();
		localTotal=0;
		System.out.println ("Stored "+grandTotal);
		
		System.out.println ("Closing DB");
		db.close();
	}
}

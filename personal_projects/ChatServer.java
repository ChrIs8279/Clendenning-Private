import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

public class ChatServer {
	private static List<ClientHandler> clients = new CopyOnWriteArrayList<>();
	public static void main(String[] args) throws IOException {
		ServerSocket serverSocket = new ServerSocket(5000);
		System.out.println("server started. Waiting for clients...");
		while(true) {
			Socket clientSocket = serverSocket.accept();
			System.out.println("Client connected: " + clientSocket);
			ClientHandler clientThread = new ClientHandler(clientSocket, clients);
			clients.add(clientThread);
			new Thread(clientThread).start();
		}
	}
}

class ClientHandler implements Runnable {
	private Socket clientSocket;
	private List<ClientHandler> clients;
	private PrintWriter out;
	private BufferedReader in;
	public ClientHandler(Socket socket, List<ClientHandler> clients) throws IOException {
		this.clientSocket=socket;
		this.clients = clients;
		this.out = new PrintWriter(clientSocket.getOutputStream(), true);
		this.in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
	}
	public void run() {
		try {
			String inputLine;
			while ((inputLine = in.readLine()) != null){
				for (ClientHandler aClient : clients) {
					aClient.out.println(inputLine);
				}
			}
		} catch (IOException e) {
			System.out.println("An error occurred: " + e.getMessage());
		} finally {
			try{
				if (in != null) in.close();
				if (out!= null) out.close();
				if (clientSocket != null) clientSocket.close();
			}catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
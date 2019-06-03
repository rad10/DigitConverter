import java.util.ArrayList;
public class DigitConverter {
	private static int power(int base, int exp){
		int result = 1;
		for(int i=0; i<exp; i++)
			result *= base;
		return result;
	}
	public static int toBin(int decimal){
		//char[] storeBin = {};
		ArrayList<Integer> storeBin = new ArrayList<Integer>();
		String result = "";
		while (decimal > 0){
			int remain = decimal%2;
			storeBin.add(remain);
			decimal = (decimal - remain)/2;
		}
		for (int i = storeBin.size()-1; i >= 0; i--)
			result = result + storeBin.get(i).toString();
		return Integer.valueOf(result);
	}
	public static int fromBin(int binary){
		String bin = String.valueOf(binary);
		int[] storeBin = new int[bin.length()];
		int result = 0;
		for (int i = 0; i < bin.length(); i++)
			storeBin[i] = Integer.valueOf(bin.substring(bin.length()-1-i,bin.length()-i));
		for (int i = 0; i < storeBin.length; i++)
			result += storeBin[i] * power(2,i);
		return result;
	}
	public static int toOct(int decimal){
		//char[] storeBin = {};
		ArrayList<Integer> storeOct = new ArrayList<Integer>();
		String result = "";
		while (decimal > 0){
			int remain = decimal%8;
			storeOct.add(remain);
			decimal = (decimal - remain)/8;
		}
		for (int i = storeOct.size()-1; i >= 0; i--)
			result = result + storeOct.get(i).toString();
		return Integer.valueOf(result);
	}
	public static int fromOct(int octal){
		String oct = String.valueOf(octal);
		int[] storeOct = new int[oct.length()];
		int result = 0;
		for (int i = 0; i < oct.length(); i++)
			storeOct[i] = Integer.valueOf(oct.substring(oct.length()-1-i,oct.length()-i));
		for (int i = 0; i < storeOct.length; i++)
			result += storeOct[i] * power(2,i);
		return result;
	}
	public static String toHex(int decimal){
		//char[] storeBin = {};
		ArrayList<Integer> storeHex = new ArrayList<Integer>();
		String result = "";
		while (decimal > 0){
			int remain = decimal%16;
			storeHex.add(remain);
			decimal = (decimal - remain)/16;
		}
		for (int i = storeHex.size()-1; i >= 0; i--){
			switch (storeHex.get(i)) {
				case 10:
					result += "A";
					break;
				case 11:
					result += "B";
					break;
				case 12:
					result += "C";
					break;
				case 13:
					result += "D";
					break;
				case 14:
					result += "E";
					break;
				case 15:
					result += "F";
					break;
				default:
					result += storeHex.get(i).toString();
					break;
			}
		}
		return result;
	}
	public static int fromHex(String hex){
		int[] storeHex = new int[hex.length()];
		int result = 0;
		for (int i = 0; i < hex.length(); i++){
			switch (hex.substring(hex.length()-1-i,hex.length()-i).toLowerCase()) {
				case "a":
					storeHex[i] = 10;
					break;
				case "b":
					storeHex[i] = 11;
					break;
				case "c":
					storeHex[i] = 12;
					break;
				case "d":
					storeHex[i] = 13;
					break;
				case "e":
					storeHex[i] = 14;
					break;
				case "f":
					storeHex[i] = 15;
					break;
				default:
					storeHex[i] = Integer.valueOf(hex.substring(hex.length()-1-i,hex.length()-i));
					break;
			}
		}
		for (int i = 0; i < storeHex.length; i++)
			result += storeHex[i] * power(16,i);
		return result;
	}
	public static void main(String[] args){
		if (args[0].equals("tobin")){
			System.out.println("ToBinary: "+args[1]);
			System.out.println(toBin(Integer.valueOf(args[1])));
		}
		else if (args[0].equals("frombin")){
			System.out.println("FromBinary: "+args[1]);
			System.out.println(fromBin(Integer.valueOf(args[1])));
		}
		else if (args[0].equals("tooct")){
			System.out.println(toOct(Integer.valueOf(args[1])));
		}
		else if (args[0].equals("fromoct")){
			System.out.println(fromOct(Integer.valueOf(args[1])));
		}
		else if (args[0].equals("tohex")){
			System.out.println(toHex(Integer.valueOf(args[1])));
		}
		else if (args[0].equals("fromhex")){
			System.out.println(fromHex(args[1]));
		}
	}
}

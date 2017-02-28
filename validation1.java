package validate;
import java.io.*;
import java.lang.*;
import java.util.*;
import com.google.common.base.CharMatcher;
import com.google.common.base.Splitter;
public class validation1{
//public static void main(String[] args)throws IOException{
public void validation() throws IOException{
File[] files=new File("/home/encoder96/readff").listFiles();
for(File file:files)
{
String file1=file.getName();
String filename=file1.substring(0,file1.indexOf("."));
String ext=".json";
filename+=ext;
File filenew=new File(filename);
if(filenew.exists())
filenew.delete();
File filenew1=new File(filename);
filenew1.createNewFile();
System.out.println("f");
FileReader f=new FileReader(file1);
Scanner sc=new Scanner(f);
StringBuffer sbi=new StringBuffer("");
sbi.append("[");
if(sbi.toString()!=null)
{
FileWriter fw=new FileWriter(filenew,true);
BufferedWriter bw=new BufferedWriter(fw);
bw.write(sbi.toString());
bw.newLine();
bw.close();	
}
while(sc.hasNextLine()) 
{
int cnt=0;
int ff=0;
sbi=new StringBuffer("");
String s=sc.nextLine();
s=s.replaceAll("//s+"," ");
String[] sb=s.split(" ");
boolean isAscii=CharMatcher.ASCII.matchesAllOf(s);
if(isAscii && !s.contains("?") && s!=null)	
{
for(int i=0;i<sb.length;i++)	
{
String ch=sb[i];
if(!ch.startsWith("RT") && !ch.startsWith("https") && !ch.startsWith("@") && ch!=null)
{
ch=ch.toLowerCase();
ch=ch.replaceAll("[^a-z]","");
if(ch.length()!=0)
{
if(cnt!=0)
{
sbi.append(",");
sbi.append("\"");
sbi.append(ch);
sbi.append("\"");
ff=1;
}
if(cnt==0)
{
sbi.append("[");
sbi.append("\"");
sbi.append(ch);
sbi.append("\"");
cnt=1;
ff=1;	
}
}
}	
}
if(ff==1)
{
sbi.append("]");
if(sc.hasNextLine())
sbi.append(",");
if(sbi.toString()!=null)
{
FileWriter fw=new FileWriter(filenew,true);
BufferedWriter bw=new BufferedWriter(fw);
bw.write(sbi.toString());
bw.newLine();
bw.close();	
}
}
}
}
if(sbi.toString()!=null)
{
FileWriter fw=new FileWriter(filenew,true);
BufferedWriter bw=new BufferedWriter(fw);
bw.write("]");
bw.newLine();
bw.close();	
}
f.close();
}	
}	
}
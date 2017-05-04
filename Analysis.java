import validate.validation1;
import java.io.*;
import java.lang.*;
import java.util.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject; 
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
//n neutral
//o oppose
//a after
public class Worddictionary1{
public Map<String,Double> dictionary;
public Map<String,String> type_conn=new HashMap<String,String>();
////////////////////////////////n neutral/////////////////////////////////////////////////
///////////////////////////////o oppose//////////////////////////////////////////////////
//////////////////////////////a after///////////////////////////////////////////////////
public void typeconnect() throws java.lang.Exception,IOException{
FileReader fr=new FileReader("connectors.txt");
BufferedReader br=new BufferedReader(fr);
String line;
String line1="",line2="";      
    while((line=br.readLine())!=null){  
           if(line.startsWith("#")){
        String[] arr=line.split("@");
        line1=arr[0];
        line2=arr[1];
        }
        else
        type_conn.put(line,line2);
    }
fr.close();
}
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
public void addwords() throws IOException,java.lang.Exception{
dictionary=new HashMap<String,Double>();
FileReader fr=new FileReader("diction1.txt");
BufferedReader bf=new BufferedReader(fr);
String line;
   while((line=bf.readLine())!=null){
        if(!line.trim().startsWith("#")){
         String[] seperate=line.split("\t");
           if((seperate.length)==4){
           String word_word=seperate[0];
           Double word_score=Double.parseDouble(seperate[1])-Double.parseDouble(seperate[2]);
           dictionary.put(word_word,word_score);
           }
        }
   }
fr.close();   
}
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
public void readjson() throws java.lang.Exception,IOException{
File fcc=new File("neww1.txt");
fcc.delete();
String sss="neww1.txt"; 
File fcb=new File(sss);
fcb.createNewFile();
File[] files=new File("/home/encoder96/readjson").listFiles();
for(File file : files){
String fff=file.getName();
FileReader inp=new FileReader(fff);
JSONParser parser=new JSONParser();
Object obj=parser.parse(inp);
JSONArray jsonArray=(JSONArray) obj;
int len=jsonArray.size();
int len1=len;
double score=0.0;
double neg_count=0.0;
double pos_count=0.0;     
String ffff=fff.substring(0,fff.indexOf("."));
for(int ii=0;ii<len;ii++){
      neg_count=0.0;
      pos_count=0.0;
      JSONArray json1=(JSONArray) jsonArray.get(ii);
      Iterator<String> iterator=json1.iterator();
      Iterator<String> iterator1=json1.iterator();
      int flag=0,cnt=0;  
      String temp="";   
          while(iterator.hasNext()){
          temp=iterator.next();
          if(type_conn.containsKey(temp) ||temp.equals("not") ||temp.equals("and")){
          flag=1;
          break;
          }
          }
      int good_first=0,bad_first=0;
          if(flag==0){
            while(iterator1.hasNext()){
            temp=iterator1.next();
                if(temp!=null){   
                for(Map.Entry<String,Double> loo:dictionary.entrySet()){
                      if(temp.equals(loo.getKey())){
                      double tmp=loo.getValue();
                         if(tmp<(double)0){
                         if(good_first==0 && bad_first==0)
                         bad_first=1; 
                         neg_count+=tmp;
                         cnt++;
                         }
                         else
                         if(tmp>(double)0){
                         if(good_first==0 && bad_first==0)
                         good_first=1;
                         pos_count+=tmp;
                         cnt++;
                         } 
                      // break;
                      } 
                }
                } 
            }  
          if(bad_first==1&&cnt!=0)
          score+=(pos_count+Math.abs(neg_count))/(double)cnt;
          else
          if(good_first==1&&cnt!=0)
          score+=(neg_count-pos_count)/(double)cnt;
          else
          if(cnt!=0)
          score+=(neg_count+pos_count)/(double)cnt;  
          }   
         else 
         {
          iterator=json1.iterator();
          String sbi="";
          String sbi1="";
          String type="";
          String word="";
          String type1=null;
          String word1="";
          while(iterator.hasNext())
          {
          String temp1=iterator.next(); 
          sbi+=temp1;
          sbi+=" ";
          if(type_conn.containsKey(temp1))
          {
          if(type!=null)
          {
          type=type_conn.get(temp1).trim();
          word=temp1.trim();
          }
          else
          { 
          type1=type_conn.get(temp1);
          word1=temp1;
          }
          }
          }

    int f=0;       
    sbi1=sbi;
double neg_p1=0.0,neg_p2=0.0,pos_p1=0.0,val1=0.0,val2=0.0;
if(type.equals("n"))
{
String temp5="";
String[] temp3;
if(type1==null)
temp3=sbi.split(word);
else
temp3=sbi.split(word1);
for(int i=0;i<2;i++)
{
f=0;
int gw=0,bw=0;
temp5=temp3[i];
String temp8=temp5;
String[] temp6=temp5.split(" ");
String temp7="";
if(temp8.contains("not") || temp8.contains("nt") || temp8.contains("neither") ||temp8.contains("nor"))
{
for(int j=0;j<temp6.length;j++)
{
neg_p1=0.0;
pos_p1=0.0;
temp7=temp6[j];
if(temp7.equals("not") || temp7.equals("nt") || temp7.equals("neither") ||temp7.equals("nor"))
f=1;
if(dictionary.containsKey(temp7))
{
double pt=dictionary.get(temp7);
if(f==1)
{
f=0;
if(pt<0)
{
neg_p1+=Math.abs(pt);
cnt++;
}
else
if(pt>0)
{
pos_p1+=(-pt);
cnt++;
}
}
else
{
if(pt<0)
{
neg_p1+=pt;
cnt++;
}
else
{
pos_p1+=pt;
cnt++;
}
}
}
}
}
else
{
for(int j=0;j<temp6.length;j++)
{
temp7=temp6[j];
double pt=0.0;
if(dictionary.containsKey(temp7))
pt=dictionary.get(temp7);
if(pt<0)
{
cnt++;
if(gw==0 && bw==0)
bw=1;
neg_p1+=pt;
}
else
if(pt>0)
{
cnt++;
if(gw==0 && bw==0)
gw=1;
pos_p1+=pt;
}
}
if(bw==1&&cnt!=0)
score+=(pos_p1+Math.abs(neg_p1))/(double)cnt;
else
if(gw==1&&cnt!=0)
score+=((neg_p1-pos_p1))/(double)cnt;
else
if(cnt!=0)
score+=(neg_p1+pos_p1)/(double)cnt;  
}
}
}
else
if(type.equals("a")) 
{
String[] temp9=sbi.split(word);
String temp10=temp9[1];
if(type1!=null)
{
if(temp10.contains(word1))
{
String[] temp11=temp10.split(word1);
for(int i=0;i<2;i++)
{
f=0;
int gw=0,bw=0;
String temp12=temp11[i];
String temp14=temp12;
String[] temp13=temp12.split(" ");
String temp15="";
if(temp14.contains("not") || temp14.contains("nt") || temp14.contains("neither") ||temp14.contains("nor") ||temp14.contains("dont"))
{
for(int j=0;j<temp13.length;j++)
{
neg_p1=0.0;
pos_p1=0.0;
temp15=temp13[j];
if(temp15.equals("not") || temp15.equals("nt") || temp15.equals("neither") ||temp15.equals("nor"))
f=1;
if(dictionary.containsKey(temp15))
{
double pt=dictionary.get(temp15);
if(f==1)
{
f=0;
if(pt<0)
{
neg_p1+=Math.abs(pt);
cnt++;
}
else
if(pt>0)
{
pos_p1+=(-pt);
cnt++;
}
}
else
{
if(pt<0)
{
neg_p1+=pt;
cnt++;
}
else
{
pos_p1+=pt;
cnt++;
}
}
}
}
}
else
{
for(int j=0;j<temp13.length;j++)
{
temp15=temp13[j];
double pt=0.0;
if(dictionary.containsKey(temp15))
pt=dictionary.get(temp15);
if(pt<0)
{
cnt++;
if(gw==0 && bw==0)
bw=1;
neg_p1+=pt;
}
else
if(pt>0)
{
cnt++;
if(gw==0 && bw==0)
gw=1;
pos_p1+=pt;
}
}
if(bw==1&&cnt!=0)
score+=(pos_p1+Math.abs(neg_p1))/(double)cnt;
else
if(gw==1&&cnt!=0)
score+=(neg_p1-pos_p1)/(double)cnt;
else
if(cnt!=0)
score+=(neg_p1+pos_p1)/(double)cnt;  
}
}
}
}
else
{
String temp17=temp10;
String[] temp16=temp10.split(" ");
f=0;
int gw=0,bw=0;
String temp18="";
if(temp17.contains("not") || temp17.contains("nt") || temp17.contains("neither") ||temp17.contains("nor"))
{
for(int j=0;j<temp16.length;j++)
{
neg_p1=0.0;
pos_p1=0.0;
temp18=temp16[j];
if(temp18.equals("not") || temp18.equals("nt") || temp18.equals("neither") ||temp18.equals("nor"))
f=1;
if(dictionary.containsKey(temp18))
{
double pt=0.0;
pt=dictionary.get(temp18);
if(f==1)
{
f=0;
if(pt<0)
{
cnt++;
neg_p1+=Math.abs(pt);
}
else
if(pt>0)
{
cnt++;
pos_p1+=(-pt);
}
}
else
{
if(pt<0)
{
cnt++;
neg_p1+=pt;
}
else
if(pt>0)
{
pos_p1+=pt;
cnt++;
}
}
}
}
}
else
{
for(int j=0;j<temp16.length;j++)
{
temp18=temp16[j];
double pt=0.0;
if(dictionary.containsKey(temp18))
pt=dictionary.get(temp18);
if(pt<0)
{
cnt++;
if(gw==0 && bw==0)
bw=1;
neg_p1+=pt;
}
else
if(pt>0)
{
cnt++;
if(gw==0 && bw==0)
gw=1;
pos_p1+=pt;
}
}
if(bw==1&&cnt!=0)
score+=(pos_p1+Math.abs(neg_p1))/(double)cnt;
else
if(gw==1&&cnt!=0)
score+=((neg_p1-pos_p1))/(double)cnt;
else
if(cnt!=0)
score+=(neg_p1+pos_p1)/(double)cnt;  
}
}
}
else
if(type.equals("o"))
{
String temp24="";  
String[] temp20=sbi.split(word);
for(int i=0;i<2;i++)
{
f=0;
int gw=0,bw=0;
temp24=temp20[i];
String temp21=temp24;
String[] temp22=temp24.split(" ");
String temp23="";
if(temp21.contains("not") || temp21.contains("nt") || temp21.contains("neither") ||temp21.contains("nor"))
{
for(int j=0;j<temp22.length;j++)
{
neg_p1=0.0;
pos_p1=0.0;
temp23=temp22[j];
if(temp23.equals("not") || temp23.equals("nt") || temp23.equals("neither") ||temp23.equals("nor"))
f=1;
if(dictionary.containsKey(temp23))
{
double pt=dictionary.get(temp23);
if(f==1)
{
f=0;
if(pt<0)
{
neg_p1+=Math.abs(pt);
cnt++;
}
else
if(pt>0)
{
cnt++;
pos_p1+=(-pt);
}
}
else
{
if(pt<0)
{
neg_p1+=pt;
cnt++;
}
else
{
pos_p1+=pt;
cnt++;
}
}
}
}
if(i==0&&cnt!=0)
val1=(neg_p1+pos_p1)/(double)cnt;
else
if(cnt!=0)
val2=(neg_p1+pos_p1)/(double)cnt;
}
else
{
for(int j=0;j<temp22.length;j++)
{
temp23=temp22[j];
double pt=0.0;
if(dictionary.containsKey(temp23))
pt=dictionary.get(temp23);
if(pt<0)
{
cnt++;
if(gw==0 && bw==0)
bw=1;
neg_p1+=pt;
}
else
if(pt>0)
{
cnt++;
if(gw==0 && bw==0)
gw=1;
pos_p1+=pt;
}
}
if(i==0&&cnt!=0)
{
if(bw==1)
val1=(pos_p1+Math.abs(neg_p1))/(double)cnt;
else
if(gw==1)
val1=((neg_p1-pos_p1))/(double)cnt;
else
val1=(neg_p1+pos_p1)/(double)cnt;  
}
else
if(cnt!=0)
{
if(bw==1)
val2=(pos_p1+Math.abs(neg_p1))/(double)cnt;
else
if(gw==1)
val2=((neg_p1-pos_p1))/(double)cnt;
else
val2=(neg_p1+pos_p1)/(double)cnt;  
}
}
}
if(val2!=0.0)
{
if(dictionary.containsKey(word))
{
if(val2<(double)0)
score+=Math.abs(dictionary.get(word));
else
score+=-(Math.abs(dictionary.get(word)));
}
else
score+=-(val2);
}
else
{
if(val1==(double)0)
score+=0.0;
else
{
if(dictionary.containsKey(word))
{
if(val1<(double)0)
score+=Math.abs(dictionary.get(word));
else
score+=-(Math.abs(dictionary.get(word)));
}
else
score+=-(val1);
}
}
}
}
}
FileWriter fw=new FileWriter("neww1.txt",true);
BufferedWriter bf=new BufferedWriter(fw); 
bf.write(ffff + " " + (double)Math.round((score/(double)len1)*1000)/1000);
bf.newLine();
bf.close();
}
}
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
  public static void main(String[] args) throws java.lang.Exception,IOException{
  Worddictionary1 dic_words=new Worddictionary1();
  validation1 val=new validation1();
  val.validation();
  dic_words.addwords();
  dic_words.typeconnect();  
  dic_words.readjson();
  }
} 

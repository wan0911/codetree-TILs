import java.util.*;
import java.io.*;

public class Main {
    public static class Node{
        Node prev, next;
        int data;
    }
    static Node head, tail;
    static int cnt;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        head = new Node();
        tail = new Node();
        int num = Integer.parseInt(br.readLine());
        for(int i = 0; i < num; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if(cmd.equals("push_front")) push_front(Integer.parseInt(st.nextToken()));
            else if(cmd.equals("push_back")) push_back(Integer.parseInt(st.nextToken()));
            else if(cmd.equals("pop_front")) pop_front();
            else if(cmd.equals("pop_back")) pop_back();
            else if(cmd.equals("size")) size();
            else if(cmd.equals("empty")) empty();
            else if(cmd.equals("front")) front();
            else back();
        }
    }

    static void push_front(int data){
        Node node = new Node();
        node.data = data;
        if(cnt == 0){
            head = node;
            tail = node;
        }
        else{
            head.prev = node;
            node.next = head;
            head = node;
        }
        cnt++;
    }

    static void push_back(int data){
        Node node = new Node();
        node.data = data;
        if(cnt == 0){
            head = node;
            tail = node;
        }
        else{
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        cnt++;
    }

    static void pop_front(){
        int data = head.data;
        if(cnt == 1){
            tail = new Node();
            head = new Node();
        }
        else{
            Node temp = head.next;
            head.next.prev = null;
            head = temp;
        }
        cnt--;
        System.out.println(data);
    }

    static void pop_back(){
        int data =tail.data;
        Node temp = tail.prev;
        if(cnt == 1){
            tail = new Node();
            head = new Node();
        }
        else{
            tail.prev.next = null;
            tail = temp;
        }
        cnt--;
        System.out.println(data);
    }

    static void size(){
        System.out.println(cnt);
    }

    static void empty(){
        System.out.println(cnt == 0 ? 1 : 0);
    }

    static void front(){
        System.out.println(head.data);
    }

    static void back(){
        System.out.println(tail.data);
    }
}
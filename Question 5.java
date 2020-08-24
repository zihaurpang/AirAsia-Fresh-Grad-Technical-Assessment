#A)
#Empty methods of function in abstract class Animal and exception is not handled correctly

#B)
public class Q5 {
    public static void main(String args[]) throws Exception {
        Fish fish = new Fish();
        fish.swim(); // works
        fish.walk(); // exception
        fish.fly(); // exception
        Bird bird = new Bird();
        bird.fly(); // works
        bird.swim(); //exception
    }
}

abstract class Animal {
    public void fly() throws Exception {
        System.out.println("Flying");
    }

    public void walk() throws Exception {
        System.out.println("Walking");
    }

    public void swim() throws Exception {
        System.out.println("Swimming");
    }
}

class Bird extends Animal {
    public void swim() throws Exception {
        throw new Exception("Not supported");
    }

}
class Fish extends Animal {
    public void walk() throws Exception {
        throw new Exception("Not supported");
    }
    public void fly() throws Exception {
        throw new Exception("Not supported");
    }
}

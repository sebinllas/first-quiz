package org.velezreyes.quiz.question6;

class DrinkImpl implements Drink{

    private String name;

    public DrinkImpl(String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    public boolean isFizzy(){
        return this.name == "ScottCola";
    }

}
package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private double insertedAmount;

  private VendingMachineImpl(){
    this.insertedAmount = 0;
  }

  private void charege(double amount) throws NotEnoughMoneyException{
    if(this.insertedAmount < amount){
      throw new NotEnoughMoneyException();
    }
    this.insertedAmount = this.insertedAmount - amount;
  }

  public void insertQuarter(){
    this.insertedAmount = this.insertedAmount + 0.25;
  }

  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException{
    if(name == "ScottCola"){
      this.charege(0.75);
      return new DrinkImpl("ScottCola");
    }
    if(name == "KarenTea"){
      this.charege(1);
      return new DrinkImpl("KarenTea");
    }
    else{
      throw new UnknownDrinkException();
    }
  }

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }
}

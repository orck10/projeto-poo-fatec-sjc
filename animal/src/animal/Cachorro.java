package animal;

public class Cachorro extends Animal{

	public Cachorro(String raca, double peso, int idade) {
		super(raca, peso, idade);
	}
	@Override
	public String fazerBarulho(){
		return " AuAu ";
	}
	
}
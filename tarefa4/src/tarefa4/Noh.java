package tarefa4;

public class Noh {
	public Object valor;
	public Noh proximo;
	
	public Noh(Object valor){
		super();
		this.valor = valor;
	}
	
	public void addNoh(Object v){
		if(this.proximo == null){
			proximo = new Noh(v);
		}
		else{
			proximo.addNoh(v);
		}
	}
	
	public String escreveNoh(){
		String str = "";
		str+= this.valor;
		if(this.proximo!=null){
			str += this.proximo.escreveNoh();
		}
		return str;
	}
	
	public static void main(String[] args){
		Noh cabeca = new Noh("a");
		cabeca.addNoh("b");
		cabeca.addNoh("c");
		System.out.println(cabeca.escreveNoh());
	}
}

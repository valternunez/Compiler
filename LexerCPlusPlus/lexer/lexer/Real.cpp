// Valter Nunez A01206138
namespace lexer;

class Real : Token {
  private:
    float value;
  public:
    Real(float value){
      this->tag = Tag.REAL
      this->value = value;
    }
    float getValue(){
      return value;
    }
}



/*
package lexer;

public class Real extends Token {
	private float value;

	public Real(float value) {
		super(Tag.REAL);
		this.value = value;
	}

	public float getValue() {
		return value;
	}
}

*/

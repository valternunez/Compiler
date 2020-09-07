// Valter Nunez A01206138
namespace pacakge;

class Integer : Token {
  private:
    int value;
  public:
    Integer(int value){
      super(Tag.INTEGER);
      this->value = value;
    }
    int getValue(){
      return value;
    }
}


/*
package lexer;

public class Integer extends Token {
	private int value;

	public Integer(int value) {
		super(Tag.INTEGER);
		this.value = value;
	}

	public int getValue() {
		return value;
	}
}
*/

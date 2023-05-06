package gr.upatras.project.junit.exerc1;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class MyClassTest {

//	@Test
//	void testExceptionIsThrown() {
//		MyClass tester = new MyClass();
//		assertThrows(IllegalArgumentException.class, () -> tester.sub(10, 5));
//	}

	@Test
	void testSub() {
		MyClass tester = new MyClass();
		assertEquals("POSITIVE", tester.sub(10, 5), "10 - 5 is positive");
	}

}


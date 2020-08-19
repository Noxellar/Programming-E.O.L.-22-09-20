using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMove : MonoBehaviour
{
	// Player rigidbody variable declaration
	Rigidbody playerRigidbody;

	// Player Input Action variable declaration
	PlayerInputActions playerInputActions;

	// Movement Input variable declaration
	Vector2 movementInput;

	// Movement Speed variable declaration
	public float movementSpeed;

	void Awake()
	{
		// Player rigidbody variable assignment
		playerRigidbody = GetComponent<Rigidbody>();

		// Player input action variable assignment to input action maps called "Player Input Actions"
		playerInputActions = new PlayerInputActions();

		// .Player is a action map and .Move is an action
		playerInputActions.Player.Move.performed += ctx => movementInput = ctx.ReadValue<Vector2>();

		// Movement Speed variable assignment in m/s
		movementSpeed = 3f;
	}

	void Update()
	{
		// Player x and y velocities. Time.deltaTime is not included because
		// movementSpeed is in already velocity: m/s
		Vector3 playerVelocityX = (transform.right * movementInput.x) * movementSpeed;
		Vector3 playerVelocityY = (transform.forward * movementInput.y) * movementSpeed;

		playerRigidbody.velocity = playerVelocityX + playerVelocityY;
	}

	void OnEnable()
	{
		playerInputActions.Enable();
	}

	void OnDisable()
	{
		playerInputActions.Disable();
	}
}

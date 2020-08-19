using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraLook : MonoBehaviour
{
	// Player Input Action variable declaration
	PlayerInputActions playerInputActions;

	// Player Object variable declaration
	GameObject player;

	// Look Input variable declaration
	Vector2 lookInput;

	void Awake()
	{
		//Player Object variable declaration
		player = GameObject.FindWithTag("Player");

		// Player input action variable assignment to input action maps called "Player Input Actions"
		playerInputActions = new PlayerInputActions();

		// Look Input variable assignment
		playerInputActions.Player.Look.performed += ctx => lookInput = ctx.ReadValue<Vector2>();

		Cursor.lockState = CursorLockMode.Confined;
		Cursor.visible = false;
	}

	void Update()
	{
		/*REMEMBER TO LOOK UP HOW TO COLLAPSE THIS CODE INTO ONE STEP*/
		Quaternion cameraRotation = transform.rotation;

		cameraRotation.x += -lookInput.y * Time.deltaTime;
		cameraRotation.x = Mathf.Clamp(cameraRotation.x, -90, 90);

		transform.rotation = cameraRotation;

		Quaternion playerRotation = player.transform.rotation;

		playerRotation.y += lookInput.x * Time.deltaTime;
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

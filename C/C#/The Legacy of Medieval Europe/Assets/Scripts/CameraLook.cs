using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraLook : MonoBehaviour
{
	// Player Input Action variable declaration
	PlayerInputActions playerInputActions;

	// Look Input and Look Sensitivity variable declaration
	Vector2 lookInput;
	float lookSensitivity;

	// Player Object variable declaration
	GameObject player;

	// Player Rotation variable declaration
	Vector3 playerRotation;

	// Camera Rotation variable declaration
	Vector3 cameraRotation;

	void Awake()
	{
		// Player input action variable assignment to input action maps called "Player Input Actions"
		playerInputActions = new PlayerInputActions();

		// Look Input and Look Sensitivity variable assignment
		playerInputActions.Player.Look.performed += ctx => lookInput = ctx.ReadValue<Vector2>();
		lookSensitivity = 10;

		// Player Object variable declaration
		player = GameObject.FindWithTag("Player");

		// Player Rotation variable declaration
		playerRotation = player.transform.eulerAngles;

		cameraRotation = transform.eulerAngles;

		Cursor.lockState = CursorLockMode.Confined;
		Cursor.visible = false;
	}

	void Update()
	{
		float playerRotationX = lookInput.x * lookSensitivity * Time.deltaTime;
		playerRotationX = playerRotation.x + playerRotationX;

		player.transform.Rotate(0, playerRotationX, 0, Space.Self);

		float cameraRotationY = lookInput.y * lookSensitivity * Time.deltaTime;
		transform.Rotate(-cameraRotationY, 0, 0, Space.Self);

		//cameraRotationY = Mathf.Clamp(cameraRotation.x + cameraRotationY, -90, 90);
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

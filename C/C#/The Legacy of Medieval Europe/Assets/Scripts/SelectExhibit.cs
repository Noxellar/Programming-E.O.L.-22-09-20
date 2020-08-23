using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class SelectExhibit : MonoBehaviour
{
	// Player Transform variable declaration
	Transform visionPosition;

	void Awake()
	{
		visionPosition = Camera.main.transform;
	}

	public void Select(InputAction.CallbackContext ctx)
	{
		RaycastHit hit;
		Physics.Raycast(visionPosition.position, visionPosition.TransformDirection(Vector3.forward), out hit, 1f);
		Debug.Log(hit.collider);
	}
}

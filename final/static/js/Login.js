function Loginformvalidation()
{

	var username=document.Login.username;
	var u_password=document.Login.u_password;

	if(Emptyfield (username,u_password))
	{
		if(validateusername(username))
		{
			if(validatepassword(u_password))
			{

					return true;

			}
		}
	return false;
}
function Emptyfield(username,u_password)
{
var username=username.value.length;
var u_password=u_password.value.length;

if (username==0|| u_password==0)
{
	alert("Fields should not be empty");
	return false;
}
else
{
	return true;
}
}

function validateusername(username)
{
	var mailformat=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;


	if(username.value.match(mailformat))
	{
		return true;
	}
	else
	{
		alert('You have to enter a valid email address!');
		username.focus();
		return false;
	}
}

function validatepassword(u_password)
{
	var u_password=/^[0-9a-zA-Z/]+$/;

	if(u_password.value.match(u_password))
	{
		return true;
	}
	else
	{
		alert('Password must have alphanumerical characters only!!');
		u_password.focus();
		return false;
	}
}
}
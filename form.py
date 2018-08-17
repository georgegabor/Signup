form = """

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td class="error">
            <input type="text" name="username" value="%(username)s"> %(usernameerror)s
          </td >
          <td >
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td class="error">
            <input type="password" name="password" value="%(password)s"> %(passworderror)s
          </td>
          <td >
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td class="error">
            <input type="password" name="verify" value="%(verify)s"> %(verifyerror)s
          </td>
          <td >
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td class="error">
            <input type="text" name="email" value="%(email)s"> %(emailerror)s
          </td>
          <td >
            
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""
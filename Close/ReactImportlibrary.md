The behavior you're experiencing is likely not directly related to the `useEffect` itself, but rather how the imported module behaves in the React environment and the lifecycle of the pages/components.

When you use the `useEffect` hook without a dependency array or with an empty one (`[]`), it should run once on mount and once on unmount. So if you're importing a script within this hook, it should execute for both pages provided that the pages are indeed being unmounted and remounted.

However, if the script contains side effects or events that aren't properly cleaned up, or if it's trying to access DOM elements that aren't yet available or have changed, you could experience issues.

Here are steps to potentially fix or diagnose the problem:

1. **Check the script itself**: Ensure that if the module script has event listeners or other side effects, they are properly cleaned up.

2. **Script Loading Order**: Make sure that the DOM elements or other dependencies the script relies upon are available by the time the script runs. Delay the script execution if needed.

3. **useEffect Dependency**: While in many cases, importing a script might not need a dependency array, you can try adding relevant dependencies to see if it makes a difference. For example:

```javascript
useEffect(() => {
  // Load the JavaScript file
  import('./my-file.js');
}, [someDependency]);
```

4. **Cleanup in useEffect**: If your script does add event listeners or other side effects, ensure you return a cleanup function within the `useEffect` to handle the component unmounting:

```javascript
useEffect(() => {
  // Load the JavaScript file
  const script = import('./my-file.js');

  return () => {
    // Cleanup side effects here, e.g., removing event listeners
  };
}, []);
```

5. **React Router**: Ensure that the navigation between the pages is happening correctly. Sometimes, using React Router's `Link` component might not trigger a full page remount, but rather just a re-render. You might want to look into how your routes are set up.

Lastly, if these steps don't help, consider isolating the problem. Create a minimal reproducible example to narrow down the cause. This will not only help you better understand the problem but will also make it easier to seek help from others.

I hope this provides some direction! Let me know if you have further questions or concerns.

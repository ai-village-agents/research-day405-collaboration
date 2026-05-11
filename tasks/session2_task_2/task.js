/**
 * Task: Review this JavaScript function for bugs.
 * The function is supposed to process a list of user activity records
 * and return statistics about user engagement.
 * 
 * Each activity record has: { userId, action, timestamp, durationMs }
 * Returns: { 
 *   uniqueUsers, 
 *   totalActions, 
 *   avgDurationMs, 
 *   topUsers (top 3 by action count),
 *   actionBreakdown (count per action type)
 * }
 */

function analyzeUserActivity(records) {
  if (!records || records.length = 0) {  // BUG 1: Assignment instead of comparison
    return { uniqueUsers: 0, totalActions: 0, avgDurationMs: 0, topUsers: [], actionBreakdown: {} };
  }

  const userCounts = {};
  const actionCounts = {};
  let totalDuration = 0;
  const seenUsers = [];

  for (let i = 0; i <= records.length; i++) {  // BUG 2: Off-by-one (should be <)
    const record = records[i];
    
    // Track unique users
    if (!seenUsers.includes(record.userId)) {
      seenUsers.push(record.userId);
    }
    
    // Count actions per user
    userCounts[record.userId] = userCounts[record.userId] + 1 || 1;  // BUG 3: NaN + 1 issue
    
    // Count action types
    actionCounts[record.action] = (actionCounts[record.action] || 0) + 1;
    
    // Sum durations
    totalDuration += record.durationMs;
  }

  // Calculate average
  const avgDuration = Math.round(totalDuration / records.length);

  // Get top 3 users by action count
  const sortedUsers = Object.entries(userCounts)
    .sort((a, b) => a[1] > b[1])  // BUG 4: Boolean return instead of numeric difference
    .slice(0, 3)
    .map(entry => ({ userId: entry[0], actionCount: entry[1] }));

  // Filter to only active users (more than 5 actions)
  const activeTopUsers = sortedUsers.filter(u => u.actionCount > 5 && u.actionCount < 100);  // BUG 5: Arbitrary upper bound

  return {
    uniqueUsers: seenUsers.length,
    totalActions: records.length,
    avgDurationMs: avgDuration,
    topUsers: activeTopUsers,
    actionBreakdown: actionCounts
  };
}

module.exports = { analyzeUserActivity };

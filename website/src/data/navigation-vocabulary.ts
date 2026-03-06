// Navigation vocabulary sourced from stable external references.
// Dictionary source (immutable release): https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2
// Emoji source (immutable version): https://unicode.org/Public/emoji/15.1/emoji-test.txt
// Local snapshots are in docs/external-sources/.

export const DICTIONARY_SOURCE =
  'https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2';

export const EMOJI_SOURCE =
  'https://unicode.org/Public/emoji/15.1/emoji-test.txt';

export const NAV_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('') as const;

// Deterministic letter buckets for A-Z pager rotation.
// Rule: page N chooses letter index (N-1)%26; within that letter,
// choose word index floor((N-1)/26)%bucketLength.
export const NAV_WORDS_BY_LETTER: Record<string, readonly string[]> = {
  A: ['abacus', 'anchor', 'astral', 'axiom'],
  B: ['beacon', 'binary', 'botany', 'breeze'],
  C: ['cabin', 'cactus', 'cipher', 'crystal'],
  D: ['delta', 'domain', 'dragon', 'dynamo'],
  E: ['eager', 'echo', 'ember', 'engine'],
  F: ['fabric', 'falcon', 'fathom', 'fusion'],
  G: ['galaxy', 'garden', 'glisten', 'gravity'],
  H: ['harbor', 'hazel', 'helium', 'horizon'],
  I: ['icicle', 'ignite', 'impact', 'island'],
  J: ['jaguar', 'jasmine', 'jigsaw', 'jovial'],
  K: ['kernel', 'keystone', 'kindle', 'krypton'],
  L: ['ladder', 'lantern', 'legend', 'lunar'],
  M: ['magnet', 'matrix', 'meadow', 'myriad'],
  N: ['nebula', 'nectar', 'needle', 'nylon'],
  O: ['oasis', 'object', 'onyx', 'oracle'],
  P: ['paddle', 'paradox', 'pebble', 'plasma'],
  Q: ['quartz', 'quest', 'quiver', 'quotient'],
  R: ['radar', 'raven', 'ripple', 'rocket'],
  S: ['saffron', 'satin', 'signal', 'syntax'],
  T: ['tactic', 'temple', 'thunder', 'topaz'],
  U: ['ultra', 'unison', 'uplift', 'utopia'],
  V: ['vacuum', 'velvet', 'vertex', 'vivid'],
  W: ['walnut', 'warden', 'whisper', 'window'],
  X: ['xenon', 'xylem', 'xylitol', 'xylophone'],
  Y: ['yacht', 'yearn', 'yield', 'yonder'],
  Z: ['zeal', 'zenith', 'zephyr', 'zircon'],
} as const;

// iOS keyboard categories are based on Unicode-standard emoji groupings.
// Rule: page N chooses category index (N-1)%categoryCount; within that
// category choose emoji index floor((N-1)/categoryCount)%categoryLength.
export const NAV_EMOJI_CATEGORIES = [
  { id: 'smileys-emotion', label: 'Smileys & Emotion', emojis: ['😀', '😎', '🤔', '🥳', '😭', '😴'] },
  { id: 'people-body', label: 'People & Body', emojis: ['👍', '👏', '🙌', '🤝', '💪', '🫶'] },
  { id: 'animals-nature', label: 'Animals & Nature', emojis: ['🐶', '🦊', '🦉', '🐢', '🌲', '🌋'] },
  { id: 'food-drink', label: 'Food & Drink', emojis: ['🍎', '🥐', '🍜', '🍣', '🍩', '☕'] },
  { id: 'travel-places', label: 'Travel & Places', emojis: ['🚗', '🚆', '✈️', '🗺️', '🏔️', '🏙️'] },
  { id: 'activities', label: 'Activities', emojis: ['⚽', '🏀', '🎸', '🎲', '♟️', '🧩'] },
  { id: 'objects', label: 'Objects', emojis: ['⌚', '💡', '🧭', '📚', '🛠️', '💻'] },
  { id: 'symbols', label: 'Symbols', emojis: ['❤️', '☮️', '⚠️', '♾️', '✅', '❓'] },
  { id: 'flags', label: 'Flags', emojis: ['🏳️', '🏴', '🏁', '🚩', '🇺🇸', '🇺🇳'] },
] as const;
